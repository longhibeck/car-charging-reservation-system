function app() {
    return {
        // State
        currentPage: 'login',
        user: null,
        cars: [],
        connectorTypes: ['TYPE_2', 'SCHUCO', 'CCS', 'CHADEMO'],
        loading: false,
        error: null,

        // Forms
        loginForm: {
            username: '',
            password: ''
        },
        carForm: {
            name: '',
            connector_types: [],
            battery_charge_limit: 80,
            battery_size: 50,
            max_kw_ac: 11,
            max_kw_dc: 50
        },

        // Initialize
        init() {
            const token = localStorage.getItem('token');
            if (token) {
                this.checkAuthStatus();
            }
        },

        // Navigation
        navigateTo(page) {
            this.currentPage = page;
            this.error = null;
        },

        // Authentication
        async login() {
            this.loading = true;
            this.error = null;

            try {
                const response = await fetch('/api/v1/auth/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.loginForm)
                });

                if (response.ok) {
                    const data = await response.json();
                    localStorage.setItem('token', data.token);
                    this.user = data.user;
                    this.navigateTo('dashboard');
                    await this.loadCars();
                } else {
                    const errorData = await response.json();
                    this.error = errorData.message || 'Login failed';
                }
            } catch (error) {
                console.error('Login error:', error);
                this.error = 'Unable to connect to login service';
            } finally {
                this.loading = false;
            }
        },

        async logout() {
            localStorage.removeItem('token');
            this.user = null;
            this.cars = [];
            this.navigateTo('login');
            this.resetForms();
        },

        async checkAuthStatus() {
            const token = localStorage.getItem('token');
            if (!token) {
                this.navigateTo('login');
                return;
            }

            try {
                const response = await fetch('/api/v1/auth/me', {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    const data = await response.json();
                    this.user = data.user;
                    this.navigateTo('dashboard');
                    await this.loadCars();
                } else {
                    this.logout();
                }
            } catch (error) {
                console.error('Auth check error:', error);
                this.logout();
            }
        },

        // Car management
        async loadCars() {
            const token = localStorage.getItem('token');
            if (!token) return;

            try {
                const response = await fetch('/api/v1/cars', {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    const data = await response.json();
                    this.cars = data.cars || [];
                } else {
                    console.error('Failed to load cars');
                }
            } catch (error) {
                console.error('Load cars error:', error);
            }
        },

        async addCar() {
            this.loading = true;
            this.error = null;

            const token = localStorage.getItem('token');
            if (!token) {
                this.logout();
                return;
            }

            try {
                const response = await fetch('/api/v1/cars', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify(this.carForm)
                });

                if (response.ok) {
                    await this.loadCars();
                    this.resetCarForm();
                    this.navigateTo('cars');
                } else {
                    const errorData = await response.json();
                    this.error = errorData.message || 'Failed to add car';
                }
            } catch (error) {
                console.error('Add car error:', error);
                this.error = 'Unable to add car';
            } finally {
                this.loading = false;
            }
        },

        // Utility functions
        resetForms() {
            this.loginForm = { username: '', password: '' };
            this.resetCarForm();
        },

        resetCarForm() {
            this.carForm = {
                name: '',
                connector_types: [],
                battery_charge_limit: 80,
                battery_size: 50,
                max_kw_ac: 11,
                max_kw_dc: 50
            };
        }
    };
}