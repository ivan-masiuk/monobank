# Определение цветов
RED=\033[0;31m
GREEN=\033[0;32m
NC=\033[0m # No Color

create_public_key:
	@echo "${GREEN}Creating keys directory if it doesn't exist...${NC}"
	mkdir -p ./keys
	@echo "${GREEN}Generating public key from private key...${NC}"
	openssl ec -in ./keys/private.pem -pubout -out ./keys/pub.pem
	@echo "${GREEN}Public key generated: ./keys/pub.pem${NC}"

create_private_key:
	@echo "${GREEN}Creating keys directory if it doesn't exist...${NC}"
	mkdir -p ./keys
	@echo "${GREEN}Generating private key using EC parameters...${NC}"
	openssl ecparam -genkey -name secp256k1 -out ./keys/private.pem
	@echo "${GREEN}Private key generated: ./keys/private.pem${NC}"

create_keys: create_private_key create_public_key
	@echo "${GREEN}Both private and public keys have been successfully created.${NC}"
