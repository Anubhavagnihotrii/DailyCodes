def partition(nums,l,r):
    pivotindex=l
    pivot=nums[l]
    i=l
    j=r
    while(i<j):
        while(nums[i]<=pivot and i<=r-1):
            i+=1
            # print(l)
        while(nums[j]>pivot and j>=l+1):
            j-=1
            # print(r)
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[pivotindex],nums[j]=nums[j],nums[pivotindex]

    return j


def quicksort(nums,left,right):
    if left<right:
            p=partition(nums,left,right)
            quicksort(nums,0,p-1)
            quicksort(nums,p+1,right)


if __name__ == '__main__':
    nums = [12, 11, 13, 5, 6, 7]
    quicksort(nums, 0, len(nums) - 1)
    print(nums)