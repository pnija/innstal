var app = angular.module('innstalApp');

app.controller('ContactController', ['$scope', '$http', '$modal', function($scope, $http, $modal){
	$scope.submit = function () {
		$http({
			method: 'POST',
			url: 'user/contact/',
			data: $scope.form
		}).then(function (response) {

		   alert('success');

		}, function (response) {

		   alert('error');

		});
	};
}])