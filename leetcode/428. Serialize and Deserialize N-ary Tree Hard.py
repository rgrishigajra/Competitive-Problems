import collections


class Codec:

    def _serializeHelper(self, root, serializedList):

        queue = collections.deque()
        queue.append(root)
        queue.append(None)

        while queue:

            # Pop a node
            node = queue.popleft()

            # If this is an "endNode", we need to add another one
            # to mark the end of the current level unless this
            # was the last level.
            if (node == None):

                # We add a sentinal value of "#" here
                serializedList.append('#')
                if queue:
                    queue.append(None)

            elif node == 'C':

                # Add a sentinal value of "$" here to mark the switch to a
                # different parent.
                serializedList.append('$')

            else:

                # Add value of the current node and add all of it's
                # children nodes to the queue. Note how we convert
                # the integers to their corresponding ASCII counterparts.
                serializedList.append(chr(node.val + 48))
                for child in node.children:
                    queue.append(child)

                # If this not is NOT the last one on the current level,
                # add a childNode as well since we move on to processing
                # the next node.
                if queue[0] != None:
                    queue.append('C')

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

        if not root:
            return ""

        serializedList = []
        self._serializeHelper(root, serializedList)
        return "".join(serializedList)

    def _deserializeHelper(self, data, rootNode):

        # We move one level at a time and at every level, we need access
        # to the nodes on the previous level as well so that we can form
        # the children arrays properly. Hence two arrays.
        prevLevel, currentLevel = collections.deque(), collections.deque()
        currentLevel.append(rootNode)
        parentNode = rootNode

        # Process the characters in the string one at a time.
        for i in range(1, len(data)):
            if data[i] == '#':

                # Special processing for end of level. We need to swap the
                # array lists. Here, we simply re-initialize the "currentLevel"
                # arraylist rather than clearing it.
                prevLevel = currentLevel
                currentLevel = collections.deque()

                # Since we move one level down, we take the parent as the first
                # node on the current level.
                parentNode = prevLevel.popleft() if prevLevel else None

            else:
                if data[i] == '$':

                    # Special handling for change in parent on the same level
                    parentNode = prevLevel.popleft() if prevLevel else None
                else:
                    childNode = Node(ord(data[i]) - 48, [])
                    currentLevel.append(childNode)
                    parentNode.children.append(childNode)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

        if not data:
            return None

        rootNode = Node(ord(data[0]) - 48, [])
        self._deserializeHelper(data, rootNode)
        return rootNode
