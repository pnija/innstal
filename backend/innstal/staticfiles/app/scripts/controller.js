
angular.module('innstal.controllers', [])
    .controller('basecontroller', function($scope, $state, $modal, $window) {
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
    })
    .controller('logincontroller', function($scope, $http, $state, $window) {
        $scope.submitted = false;

        $scope.login = function (logindata) {

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

    })
    .controller('joinincontroller', function($scope, $http, $window) {
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

                }, function (response) {
                    console.log('i am in error');
            });
        };

    })
    .controller('dashboardcontroller', function($scope, $http, $window) {
        $http({
            method: 'GET',
            url: 'user/profile/',
        }).then(function (response) {
                $scope.userid = response.data.user_id;
            }, function (response) {
                console.log('i am in error');
        });

    })
    .controller('dashboardhomecontroller', function($scope, $http, $window) {
       $scope.user_id = null;
       alert($scope.userid);
    })
    .controller('ContactController', function($scope, $http, $modal, $window, $timeout){
    
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
    })
    .controller('warrantyregistercontroller', function($scope) {
            $scope.firstName= "John";
            $scope.lastName= "Doe";
    })
    .controller('searchController', function($scope, $http, $modal, $location){
        $scope.search = function () {
            if($scope.searchText){
                var searchText = $scope.searchText

                $http({

                    method: 'GET',
                    url: 'product/search/?search='+searchText

                }).then(function (response) {
                    products = response.data;
                    $location.path("contact");
                    console.log(products);
                    $scope.products = products; 

                }, function (response) {
                    alert('error');
                });
            }
        };
    })
    .controller('bloghomecontroller', function($scope, $http, $window) {
        $http({
            method: 'GET',
            url: 'user/blog/',
        }).then(function (response) {
                $scope.blogdata = response.data;
            }, function (response) {
                console.log('i am in error');
        });
    })
    .controller('blogdetailcontroller', function($scope, $http, $window, $stateParams) {
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
    })