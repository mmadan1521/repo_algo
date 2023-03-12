
#include<stdio.h>
#include<stdlib.h>

#define left_child_idx(n)   (2 * n + 1)
#define right_child_idx(n)  (2 * n + 2)
#define parent_idx(n)       ((n - 1) / 2)

int heap[30] = {0};
int max = 0;

void print_heap(int i)
{
    for (i = 0; i < max; i++) {
        printf("%d ", heap[i]);
    }
    printf("\n");

#if 0
    int l, r;

    if (i < max) {
        printf("%d ", heap[i]);
        l = left_child_idx(i);
        print_heap(l);
        r = right_child_idx(i);
        print_heap(r);
    }
#endif
}

void add_element(int node)
{
    int i = max;
    int p;

    printf("add %d to heap\n", node);

    heap[max] = node;
    max++;

    while (i > 0) {
        p = parent_idx(i);
        //printf("parent index: %d for node index: %d\n", p, i);
        if (heap[p] > heap[i]) {
            int temp = heap[i];
            heap[i] = heap[p];
            heap[p] = temp;
        }
        i = p;
    }
}

void pop_element(int node)
{
    int i, l, r, s;

    printf("popped element: %d\n", heap[0]);

    max--;
    heap[0] =  heap[max];

    i = 0;
    while (i < max) {
        l = left_child_idx(i);
        r = right_child_idx(i);
        //printf("i=%d, l=%d, r=%d\n", heap[i], heap[l], heap[r]);
        // find the swap index 's'
        if (l >= max) {
            break;
        }
        if (r < max && heap[l] < heap[r]) {
            s = l;
        } else if (r < max && heap[l] > heap[r]) {
            s = r;
        } else {
            s = l;
        }
        if (heap[i] > heap[s]) {
            int temp = heap[i];
            heap[i] = heap[s];
            heap[s] = temp;
            i = s;
        } else {
            break;
        }
    }
}

int main()
{
    add_element(9);
    //print_heap(0);

    add_element(8);
    //print_heap(0);


    add_element(7);
    //print_heap(0);

    add_element(6);
    //print_heap(0);

    add_element(5);
    //print_heap(0);

    add_element(4);
    //print_heap(0);

    add_element(3);
    //print_heap(0);

    add_element(2);
    //print_heap(0);

    add_element(1);
    //print_heap(0);

    add_element(0);
    print_heap(0);

    pop_element(0);
    print_heap(0);

    pop_element(1);
    print_heap(0);

    pop_element(2);
    print_heap(0);

    pop_element(3);
    print_heap(0);

    pop_element(4);
    print_heap(0);

    pop_element(5);
    print_heap(0);

    pop_element(6);
    print_heap(0);

    pop_element(7);
    print_heap(0);

    pop_element(8);
    print_heap(0);

    pop_element(9);
    print_heap(0);
}
