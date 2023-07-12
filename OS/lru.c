#include <stdio.h>

int main() {
    int frames, pages, i, j, k, page_faults = 0, min;
    printf("Enter the number of frames: ");
    scanf("%d", &frames);
    int frame[frames], counter[frames];

    for (i = 0; i < frames; i++) {
        frame[i] = -1; // initialize all frames to -1
        counter[i] = 0; // initialize all counters to 0
    }

    printf("Enter the number of pages: ");
    scanf("%d", &pages);
    int page[pages];

    printf("Enter the reference string: ");
    for (i = 0; i < pages; i++) {
        scanf("%d", &page[i]);
    }

    printf("\nPage\tFrame\tPage Fault\n");
    for (i = 0; i < pages; i++) {
        printf("%d\t", page[i]);

        // check if page exists in the frame
        for (k = 0; k < frames; k++) {
            if (frame[k] == page[i]) {
                counter[k] = i + 1; // update the counter to the current time
                break;
            }
        }

        if (k == frames) { // page fault occurred
            min = counter[0];
            j = 0;
            for (k = 1; k < frames; k++) {
                if (counter[k] < min) {
                    min = counter[k];
                    j = k;
                }
            }
            frame[j] = page[i];
            counter[j] = i + 1; // update the counter to the current time
            page_faults++;
            for (k = 0; k < frames; k++) {
                printf("%d\t", frame[k]);
            }
            printf("Page Fault\n");
        }
        else { // page hit occurred
            for (k = 0; k < frames; k++) {
                printf("%d\t", frame[k]);
            }
            printf("Page Hit\n");
        }
    }

    printf("\nTotal Page Faults = %d\n", page_faults);
    return 0;
}

