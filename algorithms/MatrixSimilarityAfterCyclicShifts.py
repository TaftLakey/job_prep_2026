def areSimilar(mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        if k == 1:
            change = 1
        else:
            change = k % len(mat[0])

        if change == 0:
            return True

        temp_mat = [row[:] for row in mat]

        for i in range(len(mat)):
            if i % 2 == 1:
                for j in range(change):
                    temp = temp_mat[i].pop(-1)
                    temp_mat[i].insert(0, temp)
            else:
                for j in range(change):
                    temp = temp_mat[i].pop(0)
                    temp_mat[i].append(temp)

        if temp_mat == mat:
            return True

        return False

print(areSimilar([[1,2,3],[4,5,6],[7,8,9]], 4))
