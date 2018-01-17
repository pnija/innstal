
angular.module('innstal.controllers', [])
    .controller('basecontroller', function($scope, $rootScope, $http, $state, $modal, $window) {
        $scope.subscribe = function () {
            var params = $.param({firstname: $scope.firstname, email: $scope.subscribe_email});

            $http({
                method: 'POST',
                url: 'user/subcribe/newsletter/',
                data: params,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(function (response) {
                    $scope.firstname = '';
                    $scope.subscribe_email = '';
                }, function (response) {
                    console.log('i am in error');
            });
        };
        $rootScope.state = $state.current.name;
    })
    .controller('logincontroller', function($scope, $rootScope, $http, $state, $window, $stateParams, $modal) {

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
    .controller('joinincontroller', function($scope, $state, $rootScope, $http, $window, $modal) {
        $window.scrollTo(0, 0);
        $scope.submitted = false;

        $scope.submit = function (user) {
            $scope.user = user;

            $http({
                method: 'POST',
                url: 'user/register/',
                data: user,
            }).then(function (response) {

                    $scope.user = {};
                    $scope.regForm = {};
                    open();
                }, function (response) {
                    console.log('i am in error');
            });
        };

        function open(){
            alert('Mail has been sent to your account.');
        }

        $rootScope.state = $state.current.name;
    })
    .controller('dashboardcontroller', function($scope, $state, $rootScope, $http, $window) {
        $window.scrollTo(0, 0);
        if($window.sessionStorage.token){
            $http({
                method: 'GET',
                url: 'user/profile/',
                headers: {'Authorization': 'Token '+$window.sessionStorage.token}
            }).then(function (response) {
                    $rootScope.user_id = response.data.user.id
                }, function (response) {
                    console.log('i am in error');
            });
        }
        $rootScope.state = $state.current.name;

    })
    .controller('dashboardhomecontroller', function($scope, $state, $rootScope, $window, $http, $window) {
        $window.scrollTo(0, 0);
        $rootScope.state = $state.current.name;
    })
    .controller('ContactController', function($scope,  $state, $rootScope, $http, $modal, $window, $timeout){
    
        $window.scrollTo(0, 0);

        $scope.submit = function () {

            $scope.errors = {}
            $scope.emailFailed = {}
            $scope.sucessMessage =''

            $http({
                method: 'POST',
                url: 'user/contact/',
                data: $scope.form

            }).then(function (response) {

                $scope.sucessMessage = 'Contact Submitted Successfully'
                $scope.form = {}
                $timeout(function() { $scope.sucessMessage = ''}, 2000);

            }, function (response) {

                if(response.status == 400){
                    $scope.errors = response.data
                }

                if(response.status == 503){
                    $scope.emailFailed = response.data
                }

            });
        };
        $rootScope.state = $state.current.name;

    })
    .controller('warrantyregistercontroller', function($scope) {
            $scope.firstName= "John";
            $scope.lastName= "Doe";
    })
    .controller('searchController', function($scope, $state, $rootScope, $http, $modal, $state){
        $scope.search = function () {
            if($scope.searchText){
                $state.go("search-results",{searchText: $scope.searchText});
            }
        };
        $rootScope.state = $state.current.name;
    })
    .controller('searchResultController', function($scope, $http, $modal, $state){
        
        $scope.Text = $state.params.searchText;

        $http({

            method: 'GET',
            url: 'product/search/?search='+$scope.Text

        }).then(function (response) {
            
            $scope.products = response.data;
            console.log($scope.products)
            

        }, function (response) {
            alert('error');
        });

    })
    .controller('bloghomecontroller', function($scope, $state, $rootScope, $http, $window) {
        $window.scrollTo(0, 0);
        $http({
            method: 'GET',
            url: 'user/blog/',
        }).then(function (response) {
                $scope.blogdata = response.data;
            }, function (response){
                console.log('i am in error');
        });
        $rootScope.state = $state.current.name;

    })
    .controller('blogdetailcontroller', function($scope, $state, $rootScope, $http, $window, $stateParams) {
        $window.scrollTo(0, 0);
        if($stateParams){
            var blog_id = $stateParams.id;
            $http({
                method: 'GET',
                url: 'user/blog/'+blog_id,
            }).then(function (response) {
                    $scope.blogdetail = response.data;
                }, function (response) {
                    console.log('i am in error');
            });
        }
        $rootScope.state = $state.current.name;
    })

    .controller('warrantyregistercontroller', function($scope, $state, $http, $window) {
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
                console.log(response.data.user_profile_countries, "aaaaaaaaaaa")
            }, function (response) {
                console.log('i am in error');
        });

        $http({
            method: 'GET',
            url: 'warranty/users',
            headers: {'Authorization': 'Token '+$window.sessionStorage.token}

        }).then(function (response) {
                $scope.form = response.data[0];
                console.log(response.data[0])
            }, function (response) {
                console.log('i am in error');
        });

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
        }
        $rootScope.state = $state.current.name;
    })
    .controller('changepasswordcontroller', function($scope,  $rootScope, $http, $window, $state, $stateParams) {
        $window.scrollTo(0, 0);
        if($stateParams){
            var user_id = $stateParams.id;
            var token = $stateParams.token;
            $http({
                method: 'GET',
                url: 'user/token-check/'+user_id+'/'+token+'/',
            }).then(function (response) {

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
    .controller('profileController', function($scope, $state, $rootScope, $http, $window, $stateParams) {
        $window.scrollTo(0, 0);
        $http({
                method: 'POST',
                url: 'user/profile/',
            }).then(function (response) {
                    if(response.data.status == 'success'){

                    }
                }, function (response) {
                    console.log('i am in error');
            });
        $rootScope.state = $state.current.name;
    })
