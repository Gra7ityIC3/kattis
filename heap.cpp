#include <queue>
#include "heap.h"

std::priority_queue<int> pq;

int getMax() {
    return pq.top();
}

int getSize() {
    return pq.size();
}

void insert(int element) {
    pq.push(element);
}

void removeMax() {
    pq.pop();
}
