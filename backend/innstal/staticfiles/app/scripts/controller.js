angular.module('innstal.controllers', ['ngImgCrop'])
    .controller('basecontroller', function($scope, $rootScope, $http, $state, $modal, $window) {
        function loadCategories(){
            $http({
                method: 'GET',
                url: '/product/category/list/',
            }).then(function (response) {
                $scope.categories = response.data.categories;
            }, function (response) {
                console.log('i am in error');
            })
        }
        loadCategories()
        $rootScope.state = $state.current.name;
    })
    .controller('logincontroller', function($scope, $rootScope, $http, $state, $window,
                                            $stateParams, $modal, ngDialog) {

        $scope.inputType = 'password';
        $scope.hideShowPassword = function(){
            if ($scope.inputType == 'password')
                $scope.inputType = 'text';
            else
                $scope.inputType = 'password';
        };


        if($stateParams.id){
            $http({
                method: 'GET',
                url: 'user/account/activate/'+$stateParams.id+'/',
            }).then(function (response) {
                alert('Your account has been activated');
            }, function (response) {
                console.log('i am in error');
            });
        }

        $window.scrollTo(0, 0);
        $scope.submitted = false;
        $scope.submittedforgot = false;

        $scope.login = function (logindata) {
            console.log('logindata', logindata)
            $scope.logindata = logindata;

            $http({
                method: 'POST',
                url: 'user/login/',
                data: logindata,
            }).then(function (response) {

                $scope.logindata = {};
                $scope.loginForm = {};

                $window.sessionStorage.token = response.data.token;
                $state.go('dashboard')
            }, function (response) {
                if(response.data.status == 'failed')
                {
                    ngDialog.open({ template: '/static/app/views/alert.html',
                            className: 'ngdialog-theme-default',
                            data: {
                                status:response.data.status,
                                message: response.data.message
                            }
                        }
                    );


                }
                console.log('i am in error', response);
            });
        };


        $scope.change_password = function(data){
            if(data != null)
            {
                $http({
                    method: 'POST',
                    url: 'user/forgot-password/',
                    data: data,
                }).then(function (response) {
                    $('.forget-password').modal('hide');
                    ngDialog.open({ template: '/static/app/views/alert.html',
                            className: 'ngdialog-theme-default',
                            data: {
                                status:response.data.status,
                                message: response.data.message
                            }
                        }
                    );
                }, function (response) {
                    console.log('i am in error');
                    ngDialog.open({ template: '/static/app/views/alert.html',
                            className: 'ngdialog-theme-default',
                            data: {
                                status:response.data.status,
                                message: response.data.message
                            }
                        }
                    );
                });
            }
        }
        $rootScope.state = $state.current.name;
    })
    .controller('joinincontroller', function($scope, $state, $rootScope, $http, $window, $modal, ngDialog) {
        $window.scrollTo(0, 0);
        $scope.submitted = false;
        loadData();


        $scope.submit = function (user) {
            $scope.user = user;
            $scope.emailError = null;
            console.log('validddddddddd', $scope.regForm.$valid);
            if($scope.regForm.$valid){
                $http({
                    method: 'POST',
                    url: 'user/register/',
                    data: user,

                }).then(function (response) {
                    $scope.user = {};
                    $scope.regForm = {};
                    open();
                }, function (response) {
                    $scope.error = response.data;
                    if(response.data.status == 'failed')
                    {
                        ngDialog.open({ template: '/static/app/views/alert.html',
                                className: 'ngdialog-theme-default',
                                data: {
                                    status:response.data.status,
                                    message: response.data.message
                                }
                            }
                        );
                    }
                    console.log($scope.error)
                });
            }
        };

        function loadData(){
            $http({
                method: 'GET',
                url: 'warranty/country-list',
            }).then(function (response) {
                $scope.countries = response.data.countries;
                $scope.user_profile_countries = response.data.user_profile_countries;
                $scope.user_profile_state = response.data.user_profile_state;
                $scope.user_profile_city = response.data.user_profile_city;
            }, function (response) {
                console.log('i am in error');

            })
        }


        $scope.submitBusiness = function (businessuser) {
            console.log('busiiiiiiiiiiiiiiiiiii',businessuser)
            console.log('req', businessuser)
            $scope.businessuser = businessuser;
            $scope.emailError = null;
            if($scope.businessRegForm.$valid) {
                $http({
                    method: 'POST',
                    url: 'user/register/business-account',
                    data: businessuser,
                }).then(function (response) {
                    if(response.data['message'] == 'This domain is not allowed'){
                        $scope.wrong_domain = response.data['message']
                    }
                    if(response.data['status'] == 'success') {
                        open()
                        $state.go('business')
                    }
                    else {
                        $scope.businessuser = {};
                        $scope.businessRegForm = {};
                    }
                }, function (response) {
                    $scope.error = response.data;
                    console.log($scope.error)
                });
            }

        };

        function open(){
            alert('Mail has been sent to your account.');
        }

        $rootScope.state = $state.current.name;
    })
    .directive('passwordError', function() {
        console.log('errrrorrrrrrrrr')
        return {
            scope: false,
            require: 'ngModel',
            link: function(scope, element, attr, mCtrl) {

                function myValidation(value) {

                    if(value.length > 0){
                        if(value.length < 8 ){
                            scope.passwordError = 'Minimum eight digit required'
                            mCtrl.$setValidity('charE', false);
                        }else{
                            scope.passwordError = null;
                            mCtrl.$setValidity('charE', true);
                        }

                    }else{
                        scope.passwordError = null;
                    }
                    return value;
                }
                mCtrl.$parsers.push(myValidation);
            }
        };
    })
    .directive('repeatPasswordError', function() {
        return {
            scope: false,
            require: 'ngModel',
            link: function(scope, element, attr, mCtrl) {

                function myValidation(value) {
                    if(scope.user){
                        var password = scope.user.password;
                    }
                    else{
                        var password = scope.user_data.user.password;
                    }

                    if(value.length > 0){

                        if(value.length < 8 ){

                            scope.repeatPasswordError = 'Minimum eight digit required'
                            mCtrl.$setValidity('charE', false);

                        }else if(password != value){

                            mCtrl.$setValidity('charE', false);
                            scope.repeatPasswordError = 'Password Mismatch';

                        }else{
                            scope.repeatPasswordError = null;
                            mCtrl.$setValidity('charE', true);
                        }

                    }else{
                        scope.repeatPasswordError = null;
                    }
                    return value;
                }
                mCtrl.$parsers.push(myValidation);
            }
        };
    })
    .controller('dashboardcontroller', function($scope, $state, $rootScope, $http, $window, ngDialog) {

        $window.scrollTo(0, 0);
        if($window.sessionStorage.token){
            $http({
                method: 'GET',
                url: 'user/profile/',
                headers: {'Authorization': 'Token '+$window.sessionStorage.token}
            }).then(function (response) {
                loadCategories()
                $rootScope.user_id = response.data.user_data.user.id
            }, function (response) {
                console.log('i am in error');
                if(response.data.status == 'failed')
                {
                    ngDialog.open({ template: '/static/app/views/alert.html',
                            className: 'ngdialog-theme-default',
                            data: {
                                status:response.data.status,
                                message: response.data.message
                            }
                        }
                    );
                }
            });
        }
        $rootScope.state = $state.current.name;

        function loadCategories(){
            $http({
                method: 'GET',
                url: '/product/category/list/',
            }).then(function (response) {
                $scope.categories = response.data.categories;
                var pagesShown = 1;
                var pageSize = 4;
                $scope.paginationLimit = function(data) {
                    return pageSize * pagesShown;
                };

                $scope.hasMoreItemsToShow = function() {
                    return pagesShown < ($scope.categories.length / pageSize);
                };

                $scope.showMoreItems = function() {
                    pagesShown = pagesShown + 1;
                };
            }, function (response) {
                console.log('i am in error');
            })
        }
    })
    .controller('businesscontroller', function($scope, $state, $rootScope, $window, $http, $window) {
        $window.scrollTo(0, 0);
        // $rootScope.state = $state.current.name;
    })
    .controller('ContactController', function($scope,  $state, $rootScope, $http, $modal, $window, $timeout, ngDialog){

        $window.scrollTo(0, 0);

        $scope.submit = function () {
            $scope.errors = {}
            $scope.emailFailed = {}
            $scope.sucessMessage =''
            console.log($scope.form)
            $http({
                method: 'POST',
                url: 'user/contact/',
                data: $scope.form,

            }).then(function (response) {

                $scope.sucessMessage = 'Contact Submitted Successfully'
                $scope.form = {}
                $timeout(function() { $scope.sucessMessage = ''}, 2000);

            }, function (response) {
                console.log( response.data)
                if(response.status == 400){
                    $scope.errors = response.data
                    if(response.data.status == 'failed')
                    {
                        ngDialog.open({ template: '/static/app/views/alert.html',
                                className: 'ngdialog-theme-default',
                                data: {
                                    status:response.data.status,
                                    message: response.data.message
                                }
                            }
                        );
                    }
                    console.log($scope.errors)
                }

                if(response.status == 503){
                    $scope.emailFailed = response.data
                }

            });
        };
        $rootScope.state = $state.current.name;

    })
    .controller('searchController', function($scope, $state, $rootScope, $http, $modal, $state){
        $scope.search = function () {
            if($scope.searchText){
                $state.go("search-results",{searchText: $scope.searchText});
            }
        };
        $rootScope.state = $state.current.name;
    })
    .controller('searchResultController', function($scope, $http, $modal, $state, $window, $rootScope){

        $scope.Text = $state.params.searchText;
        $scope.products = []
        $scope.page = 0
        if($window.sessionStorage.token){
            var header = {'Authorization': 'Token '+$window.sessionStorage.token}
        }else{
            var header = {}
        }
        console.log(header)

        $scope.get_result = function(){
            $scope.page  = $scope.page + 1;

            $http({

                method: 'GET',
                url: 'product/search/?search='+$scope.Text+'&page='+$scope.page,
                headers: header

            }).then(function (response) {
                $scope.products = $scope.products.concat(response.data['results']);

                if(response.data['next'] != null){
                    $scope.next = 'true';
                }else{
                    $scope.next = null;
                }
            }, function (response) {
                alert('error');
            });
        }

        $scope.get_result();

        $scope.logout=function(){
            $http({
                method: 'GET',
                url: 'user/logout/',
                headers: {'Authorization': 'Token '+$window.sessionStorage.token}
            }).then(function (response) {
                $window.sessionStorage.clear();
                $rootScope.user_id = '';
                $state.reload();

            }, function (response) {
                console.log('i am in error');
            });
        }

        $scope.login = function(){
            var next = '/product/search-results/'+$scope.Text;
            $state.go("login-next",{next:next});
        }

    })
    .controller('bloghomecontroller', function($scope, $state, $rootScope, $http, $window, $sce) {
        $window.scrollTo(0, 0);

        $http({
            method: 'GET',
            url: 'user/blog/',
        }).then(function (response) {
            $scope.blogdata =  response.data.results;
            var htmlString = $sce.trustAsHtml($scope.blogdata[0].blog_content);
            $scope.blogdata[0].blog_content = htmlString;
        }, function (response){
            console.log('i am in error');
        });
        $rootScope.state = $state.current.name;

    })
    .controller('blogdetailcontroller', function($scope, $state, $rootScope, $http, $window, $stateParams, $sce) {
        $window.scrollTo(0, 0);
        if($stateParams){
            var blog_id = $stateParams.id;
            $http({
                method: 'GET',
                url: 'user/blog/'+blog_id,
            }).then(function (response) {
                $scope.blogdetail = response.data;
                var htmlString = $sce.trustAsHtml($scope.blogdetail.blog_content);
                $scope.blogdetail.blog_content = htmlString;
            }, function (response) {
                console.log('i am in error');
            });
        }
        $rootScope.state = $state.current.name;
    })
    .controller('changepasswordcontroller', function($scope,  $rootScope, $http, $window, $state, $stateParams, ngDialog) {
        $window.scrollTo(0, 0);
        if($stateParams){
            var user_id = $stateParams.id;
            var token = $stateParams.token;
            $http({
                method: 'GET',
                url: 'user/token-check/'+user_id+'/'+token+'/',
            }).then(function (response) {
                {
                    alert
                    ngDialog.open({ template: '/static/app/views/alert.html',
                            className: 'ngdialog-theme-default',
                            data: {
                                status:response.data.status,
                                message: response.data.message
                            }
                        }
                    );
                }

            }, function (response) {
                console.log('i am in error');
            });
        }

        $scope.changepassword = function(changedata){

            $http({
                method: 'POST',
                url: 'user/update-password/'+$stateParams.id+'/',
                data: changedata
            }).then(function (response) {
                if(response.data.status == 'success'){
                    $state.go('login')
                }
            }, function (response) {
                console.log('i am in error');
            });
        }
        $rootScope.state = $state.current.name;
    })
    .controller('profileController', function($scope, $state, $rootScope, $http, $window, $stateParams, ngDialog) {
        $scope.submitted = false;
        $scope.changed_pwd = false;

        $scope.notify = {};
        $scope.notify.subscribe = false;
        $scope.notify.message = false;
        $scope.notify.warranty = false;

        $window.scrollTo(0, 0);
        $http({
            method: 'GET',
            url: 'user/profile/',
            headers: {'Authorization': 'Token '+$window.sessionStorage.token}
        }).then(function (response) {
            console.log('User profile',response.data.user_data.password)
            $scope.user_data = response.data.user_data;
            $scope.userdata_id = response.data.user_data.id;
            $scope.userdata_countries = response.data.user_data.country;
            $scope.userdata_state = response.data.user_data.state;
            $scope.userdata_city = response.data.user_data.city;
            $scope.userdata_address = response.data.user_data.address;
            $scope.userdata_avatar = response.data.user_data.avatar;
            $rootScope.email_user = response.data.user_data.email;
            if(response.data.subscribed == true){
                $scope.subscribed = true;
                $rootScope.newsletter_pk = response.data.newsletter_pk;
            }
            else{
                $scope.subscribed = false;
            }

        }, function (response) {
            console.log('i am in error');
            if(response.data.status == 'failed')
            {
                ngDialog.open({ template: '/static/app/views/alert.html',
                        className: 'ngdialog-theme-default',
                        data: {
                            status:response.data.status,
                            message: response.data.message
                        }
                    }
                );


            }
        });
        $rootScope.state = $state.current.name;

        $http({
            method: 'GET',
            url: 'warranty/country-list',
        }).then(function (response) {
            $scope.countries = response.data.user_profile_countries;
            $scope.states = response.data.user_profile_state;
            $scope.cities = response.data.user_profile_city;
        }, function (response) {
            console.log('i am in error');
        });

        $scope.inputType = 'password';
        $scope.inputTypeConfirm = 'password';
        $scope.hideShowPassword = function(){
            if ($scope.inputType == 'password')
                $scope.inputType = 'text';
            else
                $scope.inputType = 'password';
        };

        $scope.hideShowConfirmPassword = function(){
            if ($scope.inputTypeConfirm == 'password')
                $scope.inputTypeConfirm = 'text';
            else
                $scope.inputTypeConfirm = 'password';
        };

        $scope.saveProfile = function (user_data) {
            $scope.myForm = user_data;
            var formData = new FormData();

            for (key in $scope.myForm) {
                console.log($scope.myForm[key], key)
                if (key == 'user'){
                    // formData.append(key, JSON.stringify($scope.myForm[key]))
                    formData.append(key, $scope.userdata_id)
                }
                else {
                    formData.append(key, $scope.myForm[key])
                }
            }
            formData.append("avatar", $('#fileInput')[0].files[0])
            $http({
                method: 'PUT',
                url: 'user/update/' + $scope.userdata_id + '/',
                // data: userdata,
                data: formData,
                headers: {'Authorization': 'Token ' + $window.sessionStorage.token, 'Content-Type': undefined}
            }).then(function (response) {
                $scope.email_user = userdata.user.email;
            }, function (response) {
                console.log('i am in error');
                if(response.data.status == 'failed')
                {
                    ngDialog.open({ template: '/static/app/views/alert.html',
                            className: 'ngdialog-theme-default',
                            data: {
                                status:response.data.status,
                                message: response.data.message
                            }
                        }
                    );
                }
            });
        }


        $scope.clearEmail = function(){
            $scope.errorEmail = '';
        }

        $scope.changepass = function(){
            $scope.changed_pwd = true;
        }

        $scope.saveNotification = function(notify){
            if(notify.subscribe == true){
                $http({
                    method: 'POST',
                    url: 'user/subcribe/newsletter/',
                    data: {'email': $rootScope.email_user},
                }).then(function (response) {

                }, function (response) {
                    console.log('i am in error');
                });
            }
            else{
                $http({
                    method: 'POST',
                    url: 'user/unsubcribe/newsletter/'+$rootScope.newsletter_pk,
                    data: {'email': $rootScope.email_user},
                }).then(function (response) {

                }, function (response) {
                    console.log('i am in error');
                });
            }
        }


        $scope.myImage='';
        $scope.myCroppedImage='';

        var handleFileSelect=function(evt) {
            var file=evt.currentTarget.files[0];
            var reader = new FileReader();
            reader.onload = function (evt) {
                console.log('everrrrrrrrrrrrr', evt);
                $scope.$apply(function($scope){
                    $scope.myImage=evt.target.result;
                });
            };
            reader.readAsDataURL(file);
        };
        angular.element(document.querySelector('#fileInput')).on('change',handleFileSelect);



    })
    .controller('warrantyregistercontroller', function($scope,$http, $window) {

        $scope.submitted = false;
        loadData();

        function loadData(){
            $http({
                method: 'GET',
                url: 'warranty/country-list',
            }).then(function (response) {
                $scope.countries = response.data.countries;
                $scope.companies = response.data.companies;
                $scope.product_type = response.data.product_type;
                $scope.user_profile_countries = response.data.user_profile_countries;
                $scope.user_profile_state = response.data.user_profile_state;
                $scope.user_profile_city = response.data.user_profile_city;
            }, function (response) {
                console.log('i am in error');
            });

            $http({
                method: 'GET',
                url: 'warranty/users',
                headers: {'Authorization': 'Token '+$window.sessionStorage.token}

            }).then(function (response) {
                $scope.form = response.data.results[0];
            }, function (response) {
                console.log('i am in error');
            });
        }

        $scope.submit = function (form) {
            $scope.form = form;
            console.log(form)
            var formData = new FormData();

            for( key in form){
                formData.append(key, form[key])
            }
            formData.append("warranty_image", $('#file-1')[0].files[0])
            formData.append("product", "1")



            $http({
                method: 'POST',
                url: 'warranty/register/',
                data: formData,
                headers: {'Authorization': 'Token '+$window.sessionStorage.token,
                    'Content-Type': undefined}
            }).then(function (response) {

                $scope.form = {};
                $scope.warrantyForm = {};

            }, function (response) {
                console.log('i am in error');
            });
        };

        loadRegistered();

        function loadRegistered(){
            $http({
                method: 'GET',
                url: 'warranty/register/',
                headers: {'Authorization': 'Token '+$window.sessionStorage.token}
            }).then(function (response) {

                $scope.registered_warranties = response.data.results;
                var pagesShown = 1;
                var pageSize = 4;
                $scope.paginationLimit = function(data) {
                    return pageSize * pagesShown;
                };

                $scope.hasMoreItemsToShow = function() {
                    return pagesShown < ($scope.registered_warranties.length / pageSize);
                };

                $scope.showMoreItems = function() {
                    pagesShown = pagesShown + 1;
                };
            }, function (response) {
                console.log('i am in error');
            });
        }


        $scope.loadRegisteredData = function(){
            loadData();
            loadRegistered();
        }

    })

    .controller('manualcontroller', function ($scope, $rootScope, $http, $state, $window, $stateParams, $modal, $location) {
        console.log('accessed');
    })
    .controller('loginnextcontroller', function($scope, $rootScope, $http, $state, $window, $stateParams, $modal, $location) {
        console.log('accessed');
        if($stateParams.id){
            $http({
                method: 'GET',
                url: 'user/account/activate/'+$stateParams.id+'/',
            }).then(function (response) {
                alert('Your account has been activated');
            }, function (response) {
                console.log('i am in error');
            });
        }

        $window.scrollTo(0, 0);
        $scope.submitted = false;
        $scope.submittedforgot = false;

        $scope.login = function (logindata) {
            console.log('logindata', logindata)
            $scope.logindata = logindata;

            $http({
                method: 'POST',
                url: 'user/login/',
                data: logindata,
            }).then(function (response) {

                $scope.logindata = {};
                $scope.loginForm = {};

                $window.sessionStorage.token = response.data.token;
                console.log(response.data)

                $http({
                    method: 'GET',
                    url: 'user/profile/',
                    headers: {'Authorization': 'Token '+$window.sessionStorage.token}
                }).then(function (response) {
                    $rootScope.user_id = response.data.user.id
                }, function (response) {
                    console.log('i am in error');
                });

                $location.url($state.params.next);

            }, function (response) {
                console.log('i am in error');
            });
        };

        $scope.change_password = function(data){
            if(data != null)
            {
                $http({
                    method: 'POST',
                    url: 'user/forgot-password/',
                    data: data,
                }).then(function (response) {
                    $('.forget-password').modal('hide');
                }, function (response) {
                    console.log('i am in error');
                });
            }
        }
        $rootScope.state = $state.current.name;
    })
    .controller('subscribeController', function($scope, $state, $rootScope, $http, $window, $stateParams) {
        $scope.subscribe = function (subs) {
            $http({
                method: 'POST',
                url: 'user/subcribe/newsletter/',
                data: subs,
            }).then(function (response) {
                $scope.subs = {};
            }, function (response) {
                console.log('i am in error');
            });
        };
    })
