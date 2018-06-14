import riak

myClient = riak.RiakClient(pb_port=8087)

myBucket = myClient.bucket('test')

val1 = {"Miasto" : "Warszawa", "Kraj" : "Polska"}
key1 = myBucket.new("Warszawa", data=val1)
key1.store()


output = myBucket.get("Warszawa")

if output.encoded_data:

    print("Pierwszy odczyt z bazy: \n"+output.encoded_data)
    output.data["CzyStolica"] = "Tak"
    output.store()

    if output.encoded_data:

        print("\nDrugi odczyt z bazy po update: \n"+output.encoded_data)
        print("\nUsuwanie rekordu...")
        output.delete()       

        if output.encoded_data:

            print("\nUdalo sie")
        else:
            print("\nBrak rekordu w bazie\n")

    else:
        print("\nBrak rekordu w bazie\n")

else:
    print("\nBrak rekordu w bazie\n")

