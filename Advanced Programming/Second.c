#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <unistd.h>
#include <time.h>


#define SHM_SIZE 256  // Size of the shared memory segment

typedef struct {
    char filename[200];
    char date[10];  // Format: YYYY-MM-DD
} SharedData;

// Function to check if the file is modified after the given date
int is_file_modified_after(const char *filename, const char *date) {
    struct stat file_stat;
    struct tm tm_date = {0};
    time_t file_time, input_time;

    // Convert date string to time_t
    if (strptime(date, "%Y-%m-%d", &tm_date) == NULL) {
        perror("Invalid date format");
        return -1;
    }
    input_time = mktime(&tm_date);

    // Get file metadata
    if (stat(filename, &file_stat) != 0) {
        perror("stat() failed");
        return -1;
    }
    file_time = file_stat.st_mtime;

    return difftime(file_time, input_time) > 0;  // Compare timestamps
}

// Writer process: Writes to shared memory
void writer_process(key_t key) {
    int shmid;
    SharedData *shared_data;

    // Create shared memory
    shmid = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    if (shmid < 0) {
        perror("shmget failed");
        exit(1);
    }

    // Attach shared memory
    shared_data = (SharedData *)shmat(shmid, NULL, 0);
    if (shared_data == (void *)-1) {
        perror("shmat failed");
        exit(1);
    }

    // Write data to shared memory
    printf("Enter file name: ");
    scanf("%199s", shared_data->filename);
    printf("Enter date (YYYY-MM-DD): ");
    scanf("%10s", shared_data->date);

    // Detach shared memory
    if (shmdt(shared_data) < 0) {
        perror("shmdt failed");
        exit(1);
    }

    printf("Data written to shared memory.\n");
}

// Reader process: Reads from shared memory
void reader_process(key_t key) {
    int shmid;
    SharedData *shared_data;

    // Attach shared memory
    shmid = shmget(key, SHM_SIZE, 0666);
    if (shmid < 0) {
        perror("shmget failed");
        exit(1);
    }
    shared_data = (SharedData *)shmat(shmid, NULL, 0);
    if (shared_data == (void *)-1) {
        perror("shmat failed");
        exit(1);
    }

    // Read data from shared memory
    printf("Reading data from shared memory...\n");
    printf("File name: %s\n", shared_data->filename);
    printf("Date: %s\n", shared_data->date);

    // Check file modification time
    if (is_file_modified_after(shared_data->filename, shared_data->date)) {
        printf("The file has been modified after the specified date. Displaying contents:\n");
        FILE *file = fopen(shared_data->filename, "r");
        if (file) {
            char ch;
            while ((ch = fgetc(file)) != EOF) {
                putchar(ch);
            }
            fclose(file);
        } else {
            perror("Could not open file");
        }
    } else {
        printf("The file has not been modified after the specified date.\n");
    }

    // Detach shared memory
    if (shmdt(shared_data) < 0) {
        perror("shmdt failed");
        exit(1);
    }

    // Remove shared memory
    if (shmctl(shmid, IPC_RMID, NULL) < 0) {
        perror("shmctl failed");
        exit(1);
    }
}

int main() {
    key_t key = 1234;  // Shared memory key
    int choice;

    printf("1. Writer process\n2. Reader process\n");
    printf("Select role: ");
    scanf("%d", &choice);

    if (choice == 1) {
        writer_process(key);
    } else if (choice == 2) {
        reader_process(key);
    } else {
        printf("Invalid choice.\n");
    }

    return 0;
}
