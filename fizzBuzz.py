class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result_list = []
        for i in range(1,n+1):
            div_by_3 = (i % 3) == 0
            div_by_5 = (i % 5) == 0
            no_condition = not(div_by_3 or div_by_5)

            result = "Fizz" * div_by_3 + "Buzz" * div_by_5 + str(i) * no_condition

            result_list.append(result)

        return result_list



def main() -> None:
    result = Solution().fizzBuzz(15)
    print(result)

if __name__ == "__main__":
    main()
        
