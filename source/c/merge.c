// merge.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int *arr, int *tmp, int left, int mid, int right) {
    int i = left, j = mid + 1, k = left;

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j])
            tmp[k++] = arr[i++];
        else
            tmp[k++] = arr[j++];
    }
    while (i <= mid)
        tmp[k++] = arr[i++];
    while (j <= right)
        tmp[k++] = arr[j++];
    for (int i = left; i <= right; i++)
        arr[i] = tmp[i];
}

void merge_sort(int *arr, int *tmp, int left, int right) {
    if (left >= right)
        return;
    int mid = left + (right - left) / 2;
    merge_sort(arr, tmp, left, mid);
    merge_sort(arr, tmp, mid + 1, right);
    merge(arr, tmp, left, mid, right);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "usage: merge <datafile>\n");
        return 1;
    }

    FILE *fp = fopen(argv[1], "r");
    if (!fp) {
        perror("fopen");
        return 1;
    }

    int cap = 50000;
    int *arr = malloc(cap * sizeof(int));
    int *tmp = malloc(cap * sizeof(int));
    int n = 0;

    while (fscanf(fp, "%d", &arr[n]) == 1)
        n++;
    fclose(fp);

    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    merge_sort(arr, tmp, 0, n - 1);

    clock_gettime(CLOCK_MONOTONIC, &end);

    double elapsed = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
    printf("n=%d time=%.3fs\n", n, elapsed);

    free(arr);
    free(tmp);
    return 0;
}
