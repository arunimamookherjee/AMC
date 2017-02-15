// app.js
angular.module('app', ['ui.router'])
       .config(     ['$stateProvider','$urlRouterProvider',
        function ($stateProvider,$urlRouterProvider) {
    /* configure states here */
    $stateProvider
    .state("project",{
        url:'/project',
        templateUrl:"project.html",
        controller:'newctrl',
    });
    $stateProvider
    .state("dashboard",{
        url:'/dashboard',
        templateUrl:"dashboard.html",
        controller:'dash',
    });
    $stateProvider
    .state("features",{
        url:'/features',
        templateUrl:"features.html",
    });
    $stateProvider
    .state("about",{
        url:'/about',
        templateUrl:"about.html",
    });
    $stateProvider
    .state("help",{
        url:'/help',
        templateUrl:"help.html",
    });
    $stateProvider
    .state("project2",{
    	url:'/project2',
    	templateUrl:"project2.html",
    	controller:'proctrl',
    });
    $stateProvider
    .state("preparation",{
    	url:'/preparation',
    	templateUrl:"preparation.html",
    });
     $urlRouterProvider.otherwise('/');
 }]);

