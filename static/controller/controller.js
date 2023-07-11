var mymodule=angular.module('Notificationapp',[])
mymodule.config(function($interpolateProvider) {
                $interpolateProvider.startSymbol('{[');
                $interpolateProvider.endSymbol(']}');
            });   
mymodule.controller('NotificationController',function($log,$http,$scope)
{

$scope.LoadMessage=function()
{
	$http({
		method:'GET',
		url:'/messages',
		
	}).then(function(response)
	{
		$scope.data=response.data.lists
		$scope.count=response.data['messages_count']
		
	})
}	
})