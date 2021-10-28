from actions.action import ActionBase

class ActionManager:
    def list_all_actions():
        actions_list = []
        for cls in ActionBase.__subclasses__():
            actions_list.append(cls)

        actions_list.append('Find')
        
        return actions_list
          


