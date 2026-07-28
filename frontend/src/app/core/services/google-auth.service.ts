import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../../environments/environment';
import { API } from '../constants/api.constants';
import { AuthResponse } from '../../shared/interfaces/user.interface';

declare const google: any;

@Injectable({
    providedIn: 'root'
})
export class GoogleAuthService {

    private http = inject(HttpClient);

    private scriptLoaded = false;

    loadGoogleScript(): Promise<void> {

        return new Promise((resolve, reject) => {

            // Already loaded
            if (this.scriptLoaded || (window as any).google?.accounts?.id) {
                this.scriptLoaded = true;
                resolve();
                return;
            }

            const existingScript = document.getElementById('google-client');

            if (existingScript) {

                existingScript.addEventListener('load', () => {
                    this.scriptLoaded = true;
                    resolve();
                });

                return;
            }

            const script = document.createElement('script');

            script.src = 'https://accounts.google.com/gsi/client';

            script.async = true;

            script.defer = true;

            script.id = 'google-client';

            script.onload = () => {

                this.scriptLoaded = true;

                resolve();

            };

            script.onerror = () => reject();

            document.head.appendChild(script);

        });

    }

    initializeGoogle(callback: (response: any) => void): void {

        google.accounts.id.initialize({

            client_id: environment.googleClientId,

            callback

        });

    }

    renderButton(element: HTMLElement): void {

        element.innerHTML = '';

        google.accounts.id.renderButton(element, {

            theme: 'outline',

            size: 'large',

            width: 350

        });

    }

    googleLogin(idToken: string) {

        return this.http.post<AuthResponse>(

            API.BASE_URL + API.AUTH + '/google',

            { idToken }

        );

    }

}