angular.module('app')
.controller('proctrl',['$scope','$state', function($scope,$state,$window)
	{
		$scope.goto=function(){
			$state.go('preparation',{});
			 };
	}]);
