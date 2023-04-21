# SubletNEU

## Project Description:
SubletNEU is a website that is designed for students at Northeastern and nearby universities to find sublets in Boston. A secondary use is for Renters to find Landlords around Boston. Users who look for sublets can contact students looking for a sublet through a SubletRequest, which holds data on the user and other helpful information. Renters can then accept or decline these requests. Renters in turn can submit a RentRequest to a Landlord for finding a place to rent. Only a renter can submit a rentRequest, and only a subletter can submit a subletRequest. Landlords hold the most power on the site as they can decline any kind of request, whereas Renters can only decline subletRequests proposed to them.

This project uses three containers through docker. An appsmith container holds the front-end design. The db container holds the back end databases. A web container holds the ability to communicate between the two, using Flask and python to do so. x


# Instructions for setup
# Password secrets for MySQL

You should never store passwords in a file that will be pushed to github or any other cloud-hosted system.  You'll notice that in the .gitignore, two files from this folder are indeed ignored.  

In this folder, you'll need to create two files:

- `db_password.txt`
  - in this file, put a password that will be used for a non-root db user
- `db_root_password.txt`
  - in this file, put the password you want to use for the root user (superuser) of mysql. 