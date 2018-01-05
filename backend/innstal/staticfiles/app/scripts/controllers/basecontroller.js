
var app = angular.module('innstalApp');

app.controller('basecontroller', ['$scope', '$http', function($scope, $http){

    $scope.subscribe = function () {
        var params = $.param({firstname: $scope.firstname, email: $scope.email});
        $http({
            method: 'POST',
            url: 'user/user/subcribe/',
            data: params,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        })
    };


}])


