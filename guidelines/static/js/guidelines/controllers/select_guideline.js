//
// Controller to select a guideline
//
angular.module('opal.controllers').controller(
    'SelectGuidelineCtrl', function(
        $scope, $rootScope, $modalInstance, $window, $http,
        diagnosis)
    {
        $scope.diagnosis = diagnosis;

        $scope.open_guideline = function(where){
            $http.post('/api/v0.1/guideline_consultation/', {
                where: where
            }).then(function(){
                $window.open(where, '_blank');
                $scope.cancel();
            });
        };
        
        $scope.cancel = function(){
            $modalInstance.close(null);
        };
        
    }
);
