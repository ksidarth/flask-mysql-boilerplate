## Project Description:
SubletNEU is a website that is designed for students at Northeastern and nearby universities to find sublets in Boston. A secondary use is for Renters to find Landlords around Boston. Users who look for sublets can contact students looking for a sublet through a SubletRequest, which holds data on the user and other helpful information. Renters can then accept or decline these requests. Renters in turn can submit a RentRequest to a Landlord for finding a place to rent. Only a renter can submit a rentRequest, and only a subletter can submit a subletRequest. Landlords hold the most power on the site as they can decline any kind of request, whereas Renters can only decline subletRequests proposed to them.

This project uses three containers through docker. An appsmith container holds the front-end design. The db container holds the back end databases. A web container holds the ability to communicate between the two, using Flask and python to do so.

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

youtube link: https://www.youtube.com/watch?v=ObPzfZbgqCA&feature=youtu.be




