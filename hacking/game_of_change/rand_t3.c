#include <stdio.h>

#define MAX 350
#define seed 1

int main() {
  int r[MAX];
  int i;

  r[0] = seed;
  for (i=1; i<31; i++) {
    r[i] = (16807LL * r[i-1]) % 2147483647;
    if (r[i] < 0) {
      r[i] += 2147483647;
    }
  }
  for (i=31; i<34; i++) {
    r[i] = r[i-31];
  }
  for (i=34; i<344; i++) {
    r[i] = r[i-31] + r[i-3];
    //printf("%d %d %d\n", i, r[i-31], r[i-3]);
  }
  for (i=344; i<MAX; i++) {
    r[i] = r[i-31] + r[i-3];
    //printf("%d\n", ((unsigned int)r[i]) >> 1);
  }
  for (i=0;i<50;i++) printf("%d %d\n", i, r[i]);
}
