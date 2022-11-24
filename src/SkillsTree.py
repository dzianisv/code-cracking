"""
In role-playing video games a player assumes the role of a fictional character exploring the world, completing quests and learning new skills. The skill tree is one of the systems for progressing the character's development. It represents a hierarchy of skills.
The main difficulty with such system is that whenever the player wants to learn a particular new skill, there is another skill that has to be learned first. The exception to this rule is the easiest skill to learn in the game, as it has no prerequisites. The name "skill tree" derives from the fact that those dependencies create the structure of a tree, with the easiest skill being at the root.
Once a skill is learned, the character will always have it, so there is no need to learn it again if some other skill requires it. For example, if skill 1 requires skill 0, skill 2 requires skill 1 and skill 3 requires skill 1, then in order to learn skill 2, the player needs to learn three skills: 2, 1 and 0. If the player would also like to learn skill 3, then they need to learn only one more skill, skill 3, as its prerequisites, skills 1 and 0, have already been fulfilled.
In the pictures below, red color illustrates skills that are supposed to be learned, solid edges and vertices are ones that have to be learned to unlock red ones and dashed edges and vertices are ones that can be skipped.

Write a function:

that, given an array T of N integers and an array A of M integers, returns the minimum number of skills which have to be learned to acquire all of the skills from the array A in the skill tree T.
Examples:
1. Given T = [0, 0, 1, 1] and A = [2], your function should return 3, as explained above.</p>
2. Given T = [0, 0, 0, 0, 2, 3, 3] and A = [2, 5, 6], your function should return 5. To learn skill numbers 2, 5, 6, skills T[2] = 0, T[5] = 3 and T[6] = 3 have to be learned. To learn skill number 3, skill T[3] = 0 has to be acquired. Skill 0 is the root. This gives five skills in total: 2, 5, 6, 3, 0
"""

def solution(T, A):
    learned = set()
    count = 0
    for skill in A:
        next_skill = skill
        while next_skill not in learned:
            learned.add(next_skill)
            count += 1
            next_skill = T[next_skill]

    return count
