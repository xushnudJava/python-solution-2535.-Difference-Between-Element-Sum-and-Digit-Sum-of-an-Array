class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        @author Khomidov Khushnudbek
        Tue Jan 17 5:50 PM
        2535. Difference Between Element Sum and Digit Sum of an Array
        Masala shartida ro'yhatdagi elementlar yig'indisi va shu
        elementlarni raqamlari yig'indisi o'rtasidagi farq so'ralgan
        """
        x = y = 0
        # boshlanishiga 2 ta o'zgaruvchi olip nolga tenglaymiz
        for i in nums:
            x += i
            # birinchi o'zgaruvchiga elementlarni yig'indisini
            n = i
            while n != 0:
                y += n % 10
                # ikkinchi o'zgaruvchiga elementlarni
                # raqamlar yig'indisini qo'wip ketamiz
                n //= 10
        return abs(x-y)
        # oxirida ikkalasini ayirmasini absolyut qiymatini qaytaramiz