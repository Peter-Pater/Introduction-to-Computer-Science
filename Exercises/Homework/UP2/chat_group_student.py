S_ALONE = 0
S_TALKING = 1

#==============================================================================
# Group class:
# >>>attributes:
#   - An array of items, each a Member class
#   - A dictionary that keeps who is a chat group
# >>>functions:
#    - join: first time in
#    - leave: leave the system, and the group
#    - list_my_peers: who is in chatting with me?
#    - list_all: who is in the system, and the chat groups
#    - connect: connect to a peer in a chat group, and become part of the group
#    - disconnect: leave the chat group but stay in the system
#==============================================================================

class Group:

    def __init__(self):
        self.members = {}
        self.chat_grps = {}
        self.grp_ever = 0
        self.loners_number = 0
        self.biggest_group_number = 0

    def join(self, name):
        self.members[name] = S_ALONE
        return

    # Implement this!
    def is_member(self, name):
        for key in self.members:
            if name == key:
                return True
            else:
                pass
        return False

    # Implement this!
    def leave(self, name):
        del self.members[name]
        found, group_key = self.find_group(name)
        if found == False:
            print('did not leave')
            return
        else:
            self.chat_grps[group_key].remove(name)
            if len(self.chat_grps[group_key]) == 1:
                self.members[self.chat_grps[group_key][0]] = S_ALONE
                del self.chat_grps[group_key]
        return

    # Implement this!
    def find_group(self, name):
        found = False
        group_key = 0
        for key in self.chat_grps:
            if name in self.chat_grps[key]:
                found = True
                group_key = key
                break
            else:
                pass
        return found, group_key

    # Implement this!
    def connect(self, me, peer):
        #if peer is in a group, join it
        peer_in_group, group_key = self.find_group(peer)
        self.grp_ever += 1
        if self.members[me] == S_ALONE:
            if peer_in_group == True:
                self.chat_grps[group_key].append(me)
                self.members[me] = S_TALKING
            else:
                self.chat_grps[self.grp_ever - 1] = [me, peer]
                self.members[me] = S_TALKING
                self.members[peer] = S_TALKING
        else:
            self.disconnect(me)
            if peer_in_group == True:
                self.chat_grps[group_key].append(me)
                self.members[me] = S_TALKING
            else:
                self.chat_grps[self.grp_ever - 1] = [me, peer]
                self.members[me] = S_TALKING
                self.members[peer] = S_TALKING
        return

    # Implement this!
    def disconnect(self, me):
        # find myself in the group, quit
        me_in_group, group_key = self.find_group(me)
        if me_in_group == True:
            self.chat_grps[group_key].remove(me)
            self.members[me] = S_ALONE
            if len(self.chat_grps[group_key]) == 1:
                self.members[self.chat_grps[group_key][0]] = S_ALONE
                del self.chat_grps[group_key]
        return

    def list_all(self):
        # a simple minded implementation
        full_list = "Users: ------------" + "\n"
        full_list += str(self.members) + "\n"
        full_list += "Groups: -----------" + "\n"
        full_list += str(self.chat_grps) + "\n"
        self.find_loners()
        full_list += "number of loners: -----------" + "\n"
        full_list += str(self.loners_number) + "\n"
        self.find_biggest_group()
        full_list += "the biggest group is: -----------" + "\n"
        full_list += str(self.biggest_group_number) + "\n"
        return full_list

    # Implement this!
    def list_my_peers(self, me):
        # return a list, "me" followed by other peers in my group
        my_list = []
        my_list1 = []
        me_in_group, group_key = self.find_group(me)
        if me_in_group == True:
            my_list.append(me)
            my_list1 = self.chat_grps[group_key][:]
            my_list1.remove(me)
            my_list.extend(my_list1)
        return my_list

    def find_loners(self):
        self.loners_number = 0
        for keys in self.members:
            if self.members[keys] == 0:
                self.loners_number += 1
        return

    def find_biggest_group(self):
        group_size = {}
        size = []
        keys = []
        for key in self.chat_grps:
            group_size[key] = len(self.chat_grps[key])
            size.append(len(self.chat_grps[key]))
        for key in group_size:
            if group_size[key] == max(size):
                self.biggest_group_number = key
        return
# Unit tests
if __name__ == "__main__":
    g = Group()
    g.join('a')
    g.join('b')
    print(g.list_all())
    g.connect('a', 'b')
    print(g.list_all())
    g.join('c')
    g.join('d')
    g.connect('c','d')
    print(g.list_all())
    g.join('e')
    g.connect('e','a')
    print(g.list_all())
    g.disconnect('e')
    print(g.list_all())
    # g.connect('a','c')
    # print(g.list_all())
    # g.leave('a')
    # print(g.list_all())
    # g.join('f')
    # g.connect('f','a')
    # print(g.list_all())
