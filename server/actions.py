from settings import INSTALLED_APPS


def get_server_actions():
    submodules = []
    server_actions = []
    for app in INSTALLED_APPS:
        submodules.append((__import__(f'{app}.actions')).actions)
    for submodule in submodules:
        for x in submodule.actionnames:
            server_actions.append(x)
    return server_actions

def resolve(action_name, actions=None):
    action_list = actions or get_server_actions()
    action_mapping = {
        action.get('action'): action.get('controller')
        for action in action_list
    }
    return action_mapping.get(action_name)
