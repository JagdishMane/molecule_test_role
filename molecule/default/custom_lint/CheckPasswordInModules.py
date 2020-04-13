# Custome lint test to check if any of the modules contain password parameter and no_log is not set to true
from ansiblelint import AnsibleLintRule



class CheckPasswordInModules(AnsibleLintRule):
   id = 'E5000'
   shortdesc = "Plain text password used in user module, Set no_log: True"
   description = "Plain text password used in User module. if you want to enter the plain password use no_log key"
   tags = ['password_in_user_module']
  
   def matchtask(self, file, task):
        if 'password' in task['action'].keys():
           if not 'no_log' in task.keys():
              return True
           elif not task['no_log']:
              print(task['no_log'])
              return True 
        return False 
