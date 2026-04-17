class DynamicArray {
    int* array;
    int capacity, size;
public:
    
    DynamicArray(int capacity) {
        array = new int[capacity];
        this->capacity = capacity;
        this->size = 0;
    }

    int get(int i) {
        return  array[i];
    }

    void set(int i, int n) {
        array[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) {
            resize();
        }
        array[size] = n;
        size+=1;
    }

    int popback() {
        int pop = array[size-1];
        size--;
        return pop;
    }

    void resize() {
        capacity*=2;
        int* newarr = new int[capacity];
        for(int i = 0; i < size; i++){
            newarr[i] = array[i];
        }
        delete[] array;
        array = newarr;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }

    ~DynamicArray() {
        delete[] array; 
    }
};
