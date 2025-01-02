#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>


#define MAX_CARS 20
#define MAX_ON_BRIDGE 3
#define CROSSING_TIME 2  // Time to cross the bridge in seconds

// Semaphores and variables
sem_t bridge;           // Semaphore for mutual exclusion on the bridge
sem_t direction_lock;   // To regulate direction changes
int cars_on_bridge = 0; // Cars currently on the bridge
int current_direction = 0; // 0 = no direction, 1 = direction A->B, 2 = direction B->A

typedef struct {
    int id;
    int direction;
} Car;

// Function to simulate crossing the bridge
void *car_thread(void *arg) {
    Car *car = (Car *)arg;

    for (int i = 0; i < 5; i++) { // Each car crosses the bridge 5 times
        printf("Car %d waiting to cross in direction %d\n", car->id, car->direction);

        // Ensure cars only move in one direction
        sem_wait(&direction_lock);
        if (current_direction == 0 || current_direction == car->direction) {
            current_direction = car->direction;
        }
        sem_post(&direction_lock);

        // Wait for space on the bridge
        sem_wait(&bridge);
        sem_wait(&direction_lock);
        cars_on_bridge++;
        sem_post(&direction_lock);

        printf("Car %d is crossing the bridge in direction %d (%d cars on bridge)\n",
               car->id, car->direction, cars_on_bridge);
        sleep(CROSSING_TIME);

        // Car leaves the bridge
        sem_wait(&direction_lock);
        cars_on_bridge--;
        if (cars_on_bridge == 0) {
            current_direction = 0; // Allow direction change when bridge is empty
        }
        sem_post(&direction_lock);
        sem_post(&bridge);

        printf("Car %d has crossed the bridge in direction %d\n", car->id, car->direction);
        sleep(1); // Wait before attempting to cross again
    }

    free(car);
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[MAX_CARS];
    sem_init(&bridge, 0, MAX_ON_BRIDGE);      // Allow up to MAX_ON_BRIDGE cars
    sem_init(&direction_lock, 0, 1);          // Single-direction lock

    // Create car threads
    for (int i = 0; i < MAX_CARS; i++) {
        Car *car = malloc(sizeof(Car));
        car->id = i + 1;
        car->direction = rand() % 2 + 1; // Random direction (1 or 2)

        if (pthread_create(&threads[i], NULL, car_thread, car) != 0) {
            perror("Failed to create thread");
            return 1;
        }
    }

    // Wait for all car threads to finish
    for (int i = 0; i < MAX_CARS; i++) {
        pthread_join(threads[i], NULL);
    }

    // Cleanup
    sem_destroy(&bridge);
    sem_destroy(&direction_lock);

    printf("Simulation complete.\n");
    return 0;
}
