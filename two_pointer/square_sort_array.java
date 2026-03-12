/*
Squares of a Sorted Array (Two Pointer Merge Approach | O(n) Time)

## Problem
Given a sorted integer array that may contain negative numbers, 
square each element and return the resulting array in sorted order.

Example:
Input:  [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

## Approach
1. Separate negative and positive numbeqrs.
2. Square all elements.
3. Reverse the squared negative list.
4. Merge both sorted lists using two pointers.

## Time Complexity
O(n)

## Space Complexity
O(n)
*/

package dsa_with_dedication.two_pointer;

import java.util.* ;

public class square_sort_array
{
    public static int[] square_array(int nums[])
    {
        int n=nums.length;
        List<Integer>pos =new ArrayList<>();
        List<Integer>neg =new ArrayList<>();

        for(int i=0; i < n ; i++)
        {
            if( nums[i] >= 0 )
            {
                pos.add(nums[i]);
            }
            else
            {
                neg.add(nums[i]);
            }
        }
            if(neg.isEmpty())
            {
                for(int i = 0; i < pos.size(); i++)
                {   
                    pos.set(i, pos.get(i) * pos.get(i));
                }
                return pos.stream().mapToInt(Integer::intValue).toArray();
            }
            else if(pos.isEmpty())
            {
                for(int i = 0; i < neg.size(); i++)
                {
                    neg.set(i, neg.get(i) * neg.get(i));
                }
                Collections.reverse(neg);
                return neg.stream().mapToInt(Integer::intValue).toArray();
            }
            else
            {
                int k=0; 
                int p = pos.size();
                int q = neg.size();
                int res[]=new int[p+q];

                for(int i = 0; i < pos.size(); i++)
                {
                    pos.set(i, pos.get(i) * pos.get(i));
                }

                for(int i = 0; i < neg.size(); i++)
                {
                    neg.set(i, neg.get(i) * neg.get(i));
                }
                Collections.reverse(neg);


                int i=0 , j=0 ; // initialize two pointer i for pos and j for neg .

                while(i < pos.size() && j < neg.size())
                {
                    if(pos.get(i) <= neg.get(j))
                    {
                        res[k]=pos.get(i);
                        k++;
                        i++;
                    }
                    else
                    {
                        res[k]=neg.get(j);
                        k++;
                        j++;
                    }
                }
                while( i < pos.size())
                {
                    res[k]=pos.get(i);
                    k++;
                    i++;
                }
                while( j < neg.size())
                {
                    res[k]=neg.get(j);
                    k++;
                    j++;
                }
                return res;
            }
    }
    public static void main(String[] args) {
        int arr[]=new int[]{-7,-3,2,3,11};
        int res[]=square_array(arr);

        System.out.println("the resultant array is : ");
        
        for(int i : res)
        {
            System.out.println(i);
        }
    }
}