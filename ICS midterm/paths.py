# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:00:05 2016

@author: Mebius
"""
# the grid, here it's a 4-by-4 grid, you can start with 2, or 3
size = 30
# the set that keeps the frontier of the exploration
m_map = set()
m_map.add((0, 0))
print(m_map)
print("Start: ",len(m_map))

# the dictionary records number of paths leading to a node
# e.g. paths[(0, 1)] is number of paths arriving at (0, 1)
paths = {}

#starting with just 1 pos(0,0)
while len(m_map) !=0 :
    #every time test one pos, if no new pos added, the loop terminates
    pos = m_map.pop()
    print("Current position is: ", pos)
    print(paths)
    '''
    implement your algorithm below. hints:
        - e.g. west side neighbor is (pos[0] - 1, pos[1])
        - make sure you insert newly explored nodes into the set
        -... however, the new nodes must belong to the grid!
    '''
    if pos[0] == 0 and pos[1] == 0:
        paths[pos] = 1
        m_map.add((pos[0],pos[1] + 1))
    elif pos[0] == 0:
        paths[pos] = 1
        if pos[1] < size:
            m_map.add((pos[0],pos[1] + 1))
        else:
            m_map.add((1,0))
    elif pos[1] == 0:
        paths[pos] = 1
        if pos[0] < size:
            m_map.add((pos[0] + 1,pos[1]))
        else:
            m_map.add((1,1))
    else:
        paths[pos] = paths[(pos[0]-1,pos[1])] + paths[(pos[0],pos[1]-1)]
        if pos[1] < size:
            m_map.add((pos[0],pos[1] + 1))
        elif pos[0] < size:
            m_map.add((pos[0] + 1, 1))


for p in sorted(paths.items()):
    print(p)
