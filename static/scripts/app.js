angular
	.module('addSkills', [])
	.controller('addSkillsController', ['$scope', function($scope) {

		$scope.skills = [];

		$scope.addSkill = function() {
			$scope.skills.push({'title': $scope.newSkill, 'done':false})
			$scope.newSkill = ''
		}

		$scope.deleteSkill = function(index) {
			$scope.skills.splice(index, 1);
		}
	}])