"""
1124. 表现良好的最长时间段
地址：https://leetcode-cn.com/problems/longest-well-performing-interval/

用tmp数组记录到某一天为止 之前共有多少劳累的天数，再用两层循环去算出每一个 第i天到第j天 的劳累的天数，符合条件则更新最大长度
Python 貌似会超时，用Go语言顺利通过
"""
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        tmp = []
        count = 0
        for i in hours:
            if i > 8:
                count += 1
            tmp.append(count)
        #print(tmp)
        res = 0
        if sum(tmp) == 0:
            return 0
        else:
            res = 1
        
        length = len(hours)
        for i in range(length):
            for j in range(i, length):
                if tmp[i] == tmp[j]:
                    l = 0
                elif hours[i] <= 8:
                    l = tmp[j] - tmp[i]
                else:
                    l = tmp[j] - tmp[i] + 1
                #print(i, j, l)
                if l > j - i + 1 - l:
                    #print(i , j, tmp[i], tmp[j], l)
                    res = max(res, j-i+1)
        return res



"""Go语言
func longestWPI(hours []int) int {
    var tmp []int
    count := 0
    for i := 0; i < len(hours); i++ {
        //fmt.Println(i)
        if hours[i] > 8{
            count++
            //fmt.Println(count)
        }
        tmp = append(tmp, count)
    }
    fmt.Println(tmp)
    res := 0
    
    
    length := len(hours)
    for i := 0; i < length; i++ {
        for j := i; j < length; j++ {
            l := 0
            if tmp[i] == tmp[j]{
                if tmp[i] == 0 {
                    l = 0
                } else {
                    l = 1
                }
            } else if hours[i] <= 8 {
                l = tmp[j] - tmp[i]
            } else {
                l = tmp[j] - tmp[i] + 1
            }
            if l > j - i + 1 - l {
                if j - i + 1 > res{
                    res = j - i + 1
                }
            }
        }
    }
    return res
}
"""