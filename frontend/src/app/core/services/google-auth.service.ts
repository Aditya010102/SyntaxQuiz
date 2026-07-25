import { inject, Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { AuthResponse } from '../../shared/interfaces/user.interface';
import { API } from '../constants/api.constants';
import { HttpClient } from '@angular/common/http';

declare const google: any;

@Injectable({
    providedIn: 'root'
})
export class GoogleAuthService {
    private http = inject(HttpClient);

    initializeGoogle(
        callback: (response: any) => void
    ): void {

        google.accounts.id.initialize({

            client_id: environment.googleClientId,

            callback: callback

        });

    }

    renderButton(element: HTMLElement): void {

        google.accounts.id.renderButton(

            element,

            {

                theme: 'outline',

                size: 'large',

                width: 350

            }

        );

    }

    googleLogin(idToken: string) {

        return this.http.post<AuthResponse>(

            API.BASE_URL + API.AUTH + '/google',

            {

                idToken

            }

        );

    }

}