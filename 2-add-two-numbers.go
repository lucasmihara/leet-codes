/*
type ListNode struct {
	Val int
	Next *ListNode	
}
*/
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var result ListNode
	lastNode := &result
	plusOne := false
	for ;; {
		var sum int = 0
		
		if l1 == nil && l2 == nil {
			if !plusOne {
				break
			}
		} else if l1 == nil {
			sum = l2.Val
			l2 = l2.Next
		} else if l2 == nil {
			sum = l1.Val
			l1 = l1.Next
		} else {
			sum = l1.Val + l2.Val
			l1 = l1.Next
			l2 = l2.Next
		}

		if plusOne {
			sum++
			plusOne = false
		}
		if sum >= 10 {
			plusOne = true
		}
		lastNode.Val = sum % 10
		if l1 == nil && l2 == nil && !plusOne {
			break
		}  
		var node ListNode
		lastNode.Next = &node
		lastNode = &node
	}
	return &result
}
