// Create a cache with the following interface
// Push(Pyaload, CreationTime, ExpirationTime)
// PopMinCreationTime()
// PopMinExpirationTime()


package main

import (
	"container/heap"
)

type Payload struct {
  Data string
}

type Item struct {
  	Payload *Payload
		TS int
  	index int
  	ohterItem *Item
}

type CacheHeap []*Item

func (c CacheHeap) Len() int { return len(c) }

func (c CacheHeap) Less(i, j int) bool {
  return c[i].TS < c[j].TS
}

func (c CacheHeap) Swap(i, j int) {
  c[i], c[j] = c[j], c[i]
  c[i].index = i
  c[j].index = j
}

func (c *CacheHeap) Push(item any) {
  n := len(*c)
  item := x.(*Item)
  item.index = n
  *c = append(*c, item)
}

func (c *CacheHeap) Pop() any {
  old := *c
  n = len(old)
  item := old[n-1]
  old[n-1] = nil
  item.index = -1
  *c = old[0: n-1]
  return item
}

type Cache struct {
  creationHeap CacheHeap
  expirationHeap CacheHeap
}

func NewCache() Cache {
  return Cache{make(CacheHeap), make(CacheHeap)}
}

func (c Cache) Insert(payload *Payload, creation int, expiration int) {
  creationItem = Item{payload, creation, 0, nil}
  heap.Push(&c.creationHeap, &creationItem)
  expirationItem = Item{payload, &expiration, 0, &creationItem}
  creationItem.otherItem = &expiraionItem
  heap.Push(&c.expirationHeap, &expirationItem)
}

func (c Cache) PopCreation() *Payload {
  item: = heap.Pop(&c.creationHeap).(*Item)
  heap.Remove(&c.expirationHeap, item.ohterItem.index)
  return item.Pyaload
}

func (c Cache) PopExpiration() *Payload {
  item: = heap.Pop(&c.expirationHeap).(*Item)
  heap.Remove(&c.creationHeap, item.ohterItem.index)
  return item.Payload
}


func main() {  
  c := NewCache()
  c.Insert(nil, 1, 2)
  c.Insert(nil, 1, 3)
  c.Insert(nil, 2, 4)
  c.Insert(nil, 3, 4)
  c.PopCreation()
  c.PopExpiration()
  
}

