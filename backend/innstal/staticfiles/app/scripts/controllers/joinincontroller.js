
var app = angular.module('innstalApp');

app.controller('joinincontroller', ['$scope', '$http', function($scope, $http){
    $scope.submitted = false;

    $scope.submit = function (user) {
        $scope.user = user;

        $http({
            method: 'POST',
            url: 'user/user/register/',
            data: user,
        }).then(function (response) {

//                $scope.userdata = angular.copy(user);
                $scope.user = {};
                $scope.regForm = {};

//                $modalInstance.dismiss('cancel');
            }, function (response) {
                console.log('i am in error');
//                $modalInstance.dismiss('cancel');
        });
    };

}])