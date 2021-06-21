class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        if(l1 == null) return l2;
        if(l2 == null) return l1;

        ListNode result = new ListNode(0);
        ListNode ans = result;

        while(l1 != null && l2 != null){
            if(l1.val <= l2.val){
                ans.next = l1;
                l1 = l1.next;
            }
            else{
                ans.next = l2;
                l2 = l2.next;
            }
            ans = ans.next;
        }
        ans.next = l1 != null ? l1 : l2;
        return result.next;
    }
}
