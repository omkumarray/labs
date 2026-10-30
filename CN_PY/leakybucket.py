def leaky_bucket(packets, bucket_size, rate):
    bucket = 0

    for i, incoming in enumerate(packets, 1):
        print(f"\nTime {i}")
        print(f"Incoming packet size = {incoming}")

        if bucket + incoming > bucket_size:
            dropped = bucket + incoming - bucket_size
            bucket = bucket_size
            print(f"Bucket overflow! Dropped packets = {dropped}")
        else:
            bucket += incoming
            print("Packets added successfully")

        leaked = min(bucket, rate)
        bucket -= leaked

        print(f"Packets leaked = {leaked}")
        print(f"Remaining in bucket = {bucket}")


n = int(input("Enter no. of packets: "))
packets = [int(input(f"Enter size of packet {i+1}: ")) for i in range(n)]

bucket_size = int(input("Enter bucket size: "))
rate = int(input("Enter output rate: "))

leaky_bucket(packets, bucket_size, rate)

#OUTPUT - 
#Enter no. of packets: 3
#Enter size of packet 1: 4
#Enter size of packet 2: 3
#Enter size of packet 3: 5
#Enter bucket size: 10
#Enter output rate: 2