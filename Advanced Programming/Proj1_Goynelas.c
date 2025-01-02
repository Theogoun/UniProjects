#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Θεόδωρος-Κοσμάς Γουνελάς ΑΜ:3121207
//Στέλλα Αλούση ΑΜ:3121293

void *my_realloc(void *ptr, size_t new_size) {
    // If new_size is 0, free the memory and return NULL
    if (new_size == 0) {
        free(ptr);
        return NULL;
    }

    // If ptr is NULL, this behaves like malloc
    if (ptr == NULL) {
        return malloc(new_size);
    }

    // Allocate new memory
    void *new_ptr = malloc(new_size);
    if (new_ptr == NULL) {
        // Allocation failed
        return NULL;
    }

    // Copy the old memory contents to the new memory
    // Assume old size is less than or equal to new_size
    memcpy(new_ptr, ptr, new_size); // You may need additional logic to determine the smaller size

    // Free the old memory block
    free(ptr);

    return new_ptr;
}

int main() {
    // Example usage of my_realloc
    int *arr = malloc(5 * sizeof(int));
    if (!arr) {
        perror("Initial malloc failed");
        return 1;
    }

    // Fill the array with initial values
    for (int i = 0; i < 5; i++) {
        arr[i] = i + 1;
    }

    printf("Original array: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Reallocate the array to a larger size
    arr = my_realloc(arr, 10 * sizeof(int));
    if (!arr) {
        perror("Realloc failed");
        return 1;
    }

    // Initialize new elements
    for (int i = 5; i < 10; i++) {
        arr[i] = i + 1;
    }

    printf("Resized array: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Free the memory
    free(arr);
    return 0;
}
