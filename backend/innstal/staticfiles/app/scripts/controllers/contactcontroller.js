var app = angular.module('innstalApp');

app.controller('ContactController', ['$scope', '$http', '$modal','$window', function($scope, $http, $modal, $window){
	
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

		}, function (response) {

			if(response.status == 400){
				$scope.errors = response.data
			}

			if(response.status == 503){
				$scope.emailFailed = response.data
			}

		});
	};
}])