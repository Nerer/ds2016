#ifndef SJTU_LIST_HPP
#define SJTU_LIST_HPP

#include "exceptions.hpp"

#include <cstddef>

namespace sjtu {

template<typename T>
class list {
public:
	/**
	 * see BidirectionalIterator at CppReference for help.
	 */
	class const_iterator;
	class iterator {
	private:
		/**
		 * TODO add data members
		 *   just add whatever you want.
		 */
	public:
		/**
		 * return a new iterator which pointer n-next elements
		 *   even if there are not enough elements, just return the answer.
		 * as well as operator-
		 */
		/**
		 * TODO iter++
		 */
		iterator operator++(int) {}
		/**
		 * TODO ++iter
		 */
		iterator& operator++() {}
		/**
		 * TODO iter--
		 */
		iterator operator--(int) {}
		/**
		 * TODO --iter
		 */
		iterator& operator--() {}
		/**
		 * a operator to check whether two iterators are same (pointing to the same memory).
		 */
		T& operator*() const{}
		bool operator==(const iterator &rhs) const {}
		bool operator==(const const_iterator &rhs) const {}
		/**
		 * some other operator for iterator.
		 */
		bool operator!=(const iterator &rhs) const {}
		bool operator!=(const const_iterator &rhs) const {}
		/**
		 * operator->
		 */
		T* operator->() const {}
	};
	class const_iterator {

	};
	/**
	 * TODO
	 * Constructors at least a default constructor and a copy constructor
	 */
	list() {}
	list(const list &other) {}
	/**
	 * TODO Destructor
	 */
	~list() {}
	/**
	 * TODO
	 * assignment operator
	 */
	list &operator=(const list &other) {}
	/**
	 * access the first element
	 * throw container_is_empty when it is empty.
	 */
	const T & front() const {}
	/**
	 * access the last element
	 * throw container_is_empty when it is empty.
	 */
	const T & back() const {}
	/**
	 * returns an iterator to the beginning.
	 */
	iterator begin() {}
	const_iterator cbegin() const {}
	/**
	 * returns an iterator to the end.
	 */
	iterator end() {}
	const_iterator cend() const {}
	/**
	 * checks whether the container is empty.
	 */
	bool empty() const {}
	/**
	 * returns the number of elements.
	 */
	size_t size() const {}
	/**
	 * clears the contents.
	 */
	void clear() {}
	/**
	 * inserts value before pos.
	 * returns an iterator pointing to the insert value.
	 */
	iterator insert(iterator pos, const T &value) {}
	/**
	 * removes the element at pos.
	 * returns an iterator following the last removed element.
	 * If there was anything wrong with the iterator, throw invalid_iterator.
	 * If the iterator pos refers to the last element, the end() iterator is returned.
	 */
	iterator erase(iterator pos) {}
	/**
	 * removes the elements in range [first, last).
	 * returns an iterator following the last removed element.
	 * If there was anything wrong with these iterators, throw invalid_iterator.
	 * In this case, return last.
	 */
	iterator erase(iterator first, iterator last) {}
	/**
	 * adds an element to the end
	 */
	void push_back(const T &value) {}
	/**
	 * removes the last element.
	 */
	void pop_back() {}
	/**
	 * adds an element to the beginning
	 */
	void push_front(const T &value) {}
	/**
	 * removes the first element.
	 */
	void pop_front() {}
};

}

#endif