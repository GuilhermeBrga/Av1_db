from hash.bucket import Bucket
import time

class HashIndex:
    def __init__(self, nb, fr):
        self.nb = nb
        self.fr = fr
        self.buckets = [Bucket(fr) for _ in range(nb)]
        self.collisions = 0
        self.overflow_count = 0

    def hash_function(self, key):
        return hash(key) % self.nb

    def insert(self, key, page_number):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        while True:
            if not bucket.is_full():
                bucket.entries.append((key, page_number))
                return
            else:
                self.collisions += 1

                if bucket.overflow is None:
                    bucket.overflow = Bucket(self.fr)
                    self.overflow_count += 1

                bucket = bucket.overflow

    def build_index(self, page_manager):
        current = page_manager.first

        while current is not None:
            page_number = current.get_character()

            for word in current.get_register():
                self.insert(word, page_number)

            current = current.next

    def search(self, key):
        start_time = time.perf_counter()
        index = self.hash_function(key)
        bucket = self.buckets[index]
        buckets_accessed = 0

        while bucket is not None:
            buckets_accessed += 1
            for k, page_number in bucket.entries:
                if k == key:
                    end_time = time.perf_counter()
                    return page_number, buckets_accessed, (end_time - start_time)
            bucket = bucket.overflow

        end_time = time.perf_counter()
        return None, buckets_accessed, (end_time - start_time)

    def collision_rate(self, total_records):
        return (self.collisions / total_records) * 100

    def overflow_rate(self):
        return (self.overflow_count / self.nb) * 100