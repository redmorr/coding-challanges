import cProfile

import dp
import recursion
import combination

cProfile.run('dp.Solution().uniquePaths(10000, 1000 )')
cProfile.run('recursion.Solution().uniquePaths(10000, 1000 )')
cProfile.run('combination.Solution().uniquePaths(10000, 10000 )')
