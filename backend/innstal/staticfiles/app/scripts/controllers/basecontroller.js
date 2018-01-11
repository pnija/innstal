
var app = angular.module('innstalApp', ['ui.bootstrap']);

app.controller('basecontroller', ['$scope', '$http', '$modal', function($scope, $http, $modal){
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

}])


