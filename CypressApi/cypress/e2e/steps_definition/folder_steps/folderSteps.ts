
import {When} from "@badeball/cypress-cucumber-preprocessor";
import {config} from '@config/config';


 const BASE_URL = Cypress.env('base_url') as string;
const CREATE_FOLDER_URL = config.url.folder.create_folder

When('Create Folder', () => {
    cy.fixture('folders/create_folder.json').then((body) =>{
        cy.sentRequest('post', `${BASE_URL}/${CREATE_FOLDER_URL}`, body);
    })
});