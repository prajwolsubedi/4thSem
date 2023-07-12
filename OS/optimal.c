#include <stdio.h>

int main() {
    int frames, pages, i, j, k, max, page_faults = 0, found = 0;
    printf("Enter the number of frames: ");
    scanf("%d", &frames);
    int frame[frames], future[frames], page[frames], temp[frames];

    for (i = 0; i < frames; i++) {
        frame[i] = -1; // initialize all frames to -1
        future[i] = -1; // initialize all future indices to -1
    }

    printf("Enter the number of pages: ");
    scanf("%d", &pages);

    printf("Enter the reference string: ");
    for (i = 0; i < pages; i++) {
        scanf("%d", &page[i]);
    }

    printf("\nPage\tFrame\tPage Fault\n");
    for (i = 0; i < pages; i++) {
        printf("%d\t", page[i]);

        found = 0;
        // check if page exists in the frame
        for (j = 0; j < frames; j++) {
            if (frame[j] == page[i]) {
                found = 1;
                break;
            }
        }

        if (found == 0) { // page fault occurred
            max = -1;
            for (j = 0; j < frames; j++) {
                temp[j] = -1;
                for (k = i + 1; k < pages; k++) {
                    if (frame[j] == page[k]) {
                        temp[j] = k;
                        break;
                    }
                }
                if (temp[j] == -1) {
                    max = j;
                    break;
                }
                if (temp[j] > future[j]) {
                    future[j] = temp[j];
                    max = j;
                }
            }
            frame[max] = page[i];
            future[max] = -1;
            page_faults++;
            for (j = 0; j < frames; j++) {
                printf("%d\t", frame[j]);
            }
            printf("Page Fault\n");
        }
        else { // page hit occurred
            for (j = 0; j < frames; j++) {
                printf("%d\t", frame[j]);
            }
            printf("Page Hit\n");
        }
    }

    printf("\nTotal Page Faults = %d\n", page_faults);
    return 0;
}

