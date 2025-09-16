from tail_recursive import tail_recursive
# recursive function that gets list of lists, sorts them and zips them together
def sortedzip(lists):
    def sort_list(ls): 
        if not ls:
            return ()
        return (sorted(ls[0]),) + sort_list(ls[1:])
    return (zip(*sort_list(lists)))

# tail recursive function that gets list of lists, sorts them and zips them together
def sortedzip_tail(lists):
    @tail_recursive
    def sort_list(ls, acc=()): 
        if not ls:
            return acc
        return sort_list.tail_call(ls[1:], acc + (sorted(ls[0]),))
    return (zip(*sort_list(lists)))

# usage
print(
    list(sortedzip([[3,1,2],[5,6,4],['a','b','c']]))
)
print(
    list(sortedzip_tail([[3,1,2],[5,6,4],['a','b','c']]))
    )