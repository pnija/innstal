
var app = angular.module('innstalApp');

app.controller('logincontroller', ['$scope', '$http', function($scope, $http){
    $scope.submitted = false;

    $scope.login = function (logindata) {
        $scope.logindata = logindata;

        $http({
            method: 'POST',
            url: 'user/login/',
            data: logindata,
        }).then(function (response) {
                $scope.user = {};
                console.log(response);
//                $modalInstance.dismiss('cancel');
            }, function (response) {
                console.log('i am in error');
//                $modalInstance.dismiss('cancel');
        });
    };

}])