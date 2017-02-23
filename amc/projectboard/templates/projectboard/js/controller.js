angular.module('app')
.controller('newctrl',['$scope','$state', function($scope,$state,$window)
	{
		$scope.click=function(){
			
			$state.go("preparation",{});
		
        };
	}]);

