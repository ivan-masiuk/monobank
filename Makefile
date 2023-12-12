create_private_key:
	 openssl ecparam -genkey -name secp256k1 -in /dev/urandom -out ../keys/private.pem
create_public_key:
	openssl ec -in private.pem -pubout -out ../keys/pub.pem
